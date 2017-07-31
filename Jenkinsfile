#!/usr/bin/env groovy
import static groovy.io.FileType.DIRECTORIES

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
                 if (env.BRANCH_NAME == 'master') {
		             checkout([
						$class: 'GitSCM',
						branches: [[name: 'master']],
						doGenerateSubmoduleConfigurations: false,
						extensions: [],
						submoduleCfg: [],
						userRemoteConfigs: [[credentialsId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
						refspec: '+refs/heads/master:refs/remotes/origin/master',
						url: 'https://github.com/Thenmozhy/mnc_jenkinsfile/']]
			         ])
                }else {
		               checkout([
						$class: 'GitSCM',
						branches: [[name: 'develop']],
						doGenerateSubmoduleConfigurations: false,
						extensions: [],
						submoduleCfg: [],
						userRemoteConfigs: [[credentialsId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
						refspec: '+refs/heads/develop:refs/remotes/origin/develop',
						url: 'https://github.com/Thenmozhy/mnc_jenkinsfile/']]
					])	
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
			   if (env.BRANCH_NAME == 'master') {
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
