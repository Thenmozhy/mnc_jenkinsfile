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
			checkout([
			  $class: 'GitSCM',
			  branches: [[name: 'master']],
			  userRemoteConfigs: [[credentialsId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
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
			try {
			  sh '''
                  #!/bin/bash
				  set -e
				  aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://thenmozhy-test-buck/REAN-ManagedCloud-DEV/master/REAN-ManagedCloud-repo.zip --recursive
				  echo "artifacts sent to master"
                '''
			}
			catch (Exception e) {
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
