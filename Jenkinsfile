#!/usr/bin/env groovy

def setJobProperties() {
  properties([
    [
      $class: 'GithubProjectProperty',
      displayName: 'Test',
      projectUrlStr: 'https://github.com/Thenmozhy/mnc_jenkinsfile/'
    ],
    [
      $class: 'BuildDiscarderProperty',
      strategy: [
        $class: 'BuildRotator',
        daysToKeep: 5,
        numToKeep: 10,
        artifactsDaysToKeep: 5,
        artifactsNumToKeep: 10
      ]
    ],
    pipelineTriggers([
      [
        $class: 'GitHubPRTrigger',
        spec: '',
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
 					  
  
	stage('clone__master_repo') {
	  steps {
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
	   }
	}
	
	stage('clone_develop_repo') {
	  steps {
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
	
	stage('archive_repo') {
	  steps {
	        echo "Archiving the cloned repo"
			    script {
			    try {
			      sh '''
		 	          #!/bin/bash
					  ls -l
					  b=$(git show :/^Merge)
					  echo "$b"
					  c=$(git branch --merged )
					  echo "$c"
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
				        aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://thenmozhy-test-buck/REAN-ManagedCloud-DEV/Develop/REAN-ManagedCloud-repo.zip 
				        echo "artifacts sent to master"
                      '''
				}else{
			        sh '''
                        #!/bin/bash
				        set -e
				        aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://thenmozhy-test-buck/REAN-ManagedCloud-DEV/Develop/REAN-ManagedCloud-repo.zip 
				        echo "artifacts sent to develop"
                      '''
                }
		    }
	    }
	 }	
  }  
}
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
