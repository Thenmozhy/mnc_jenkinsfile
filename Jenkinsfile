#!/usr/bin/env groovy
import static groovy.io.FileType.DIRECTORIES

def setJobPropertiesVerify() {
    properties([
    [
      $class: 'GithubProjectProperty',
      displayName: 'Test',
      projectUrlStr: 'https://github.com/Thenmozhy/mnc_jenkinsfile/'
    ],
    pipelineTriggers([
      [
        $class: 'GhprbTrigger',
		    gitHubAuthId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
		    adminlist: 'pveerannagari',
		    useGitHubHooks: true,
		    cron: '* * * * *',
		    orgslist: 'reancloud',
		    allowMembersOfWhitelistedOrgsAsAdmin: true,
		    extensions: [[
		      $class: 'GhprbSimpleStatus',
		      commitStatusContext: 'Uploading artifacts',
		      triggeredStatus: 'build triggered',
		      startedStatus: 'build started',
		      completedStatus: [[
		        result: 'SUCCESS',
			      message: 'Uploading the artifacts to S3 bucket success',
			      result: 'FAILURE',
			      message: 'Uploading the artifacts to S3 bucket failed'
		      ]]
		   ]]
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
	  
	stage('clone_repo') {
	  steps {
            echo "find the branch"
			    script {
			    try {
			      sh '''
                      #!/bin/bash
					  ${ghprbActualCommit}
                      a=$(git diff-tree --name-only ${ghprbActualCommit})
					  echo "$a"
					  b=$(git show :/^Merge)
					  echo "$b"
					  c=$(git branch --merged )
					  echo "$c"
                }
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
  }  
}
