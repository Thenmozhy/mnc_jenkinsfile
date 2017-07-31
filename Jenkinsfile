#!/usr/bin/env groovy
import static groovy.io.FileType.DIRECTORIES
def branch = ${BRANCH_NAME}
def commit = ${GIT_COMMIT}

def setJobPropertiesVerify() {
	pipelineTriggers([
      [
        $class: 'GitHubPushTrigger',
        spec: '',
		pollSCM: '* * * * *',
        triggerMode: 'HEAVY_HOOKS',
        events: [[
            $class: 'GitHubPROpenEvent'
        ]],
        abortRunning: true,
        branchRestriction: ([
          targetBranch: 'develop\nmaster'
        ]),
        preStatus: true,
        skipFirstRun: true
      ]
	 ]) 
}

pipeline {
  agent {
    node {
      label 'master'
      customWorkspace 'workspace/REAN-ManagedCloud-DEV'
    }
  }
    
  stages {
    stage('Clean the workspace before build'){
      steps{
        script{
              step([$class: 'WsCleanup'])
          }
        }
      }  
	  
  stage('clone_repo') {
	steps {
	     script {
		    try {
			  sh '''
			      #!/bin/bash
				  git_branch=$(git symbolic-ref HEAD 2>/dev/null)
				  echo "$git_branch"
                  
                '''
			}
			catch (Exception e) {
			}
                 
			}
		}
	}
 
   stage('archive_repo') {
	  steps {
	        echo "Archiving the cloned repo"
			script {
			try {
			  sh '''
			      #!/bin/bash
				  ls -l
                  zip -r "$WORKSPACE/REAN-ManagedCloud-repo.zip" /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV -x *.git*
                '''
			}
			catch (Exception e) {
			}
		  }				  
	    }
	  }
	
    stage('Uploading the artifacts to S3 bucket') {
	  steps {
			echo "Starting verify target branch"
			script {
			   if (env.ref == 'refs/heads/master') {
			        sh '''
                        #!/bin/bash
				        set -e
				        aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://thenmozhy-test-buck/REAN-ManagedCloud-DEV/Develop/REAN-ManagedCloud-repo.zip --recursive
				        echo "artifacts sent to master"
                      '''
				}else{
			        sh '''
                        #!/bin/bash
				        set -e
				        aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://thenmozhy-test-buck/REAN-ManagedCloud-DEV/Develop/REAN-ManagedCloud-repo.zip --recursive
				        echo "artifacts sent to develop"
                      '''
                }
		    }
	    }
	 }	
  } 
  post {
    always {
      deleteDir()
    }
  } 
} 
