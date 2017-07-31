pipeline {
  agent {
    node {
      label 'master'
      customWorkspace 'workspace/REAN-ManagedCloud-DEV/'
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
	  
	stage('lastest merge') {
	  steps {
	        echo "Branch have latest merge"
			script {
			try {
			  sh '''
			      #!/bin/bash
				  pwd
				  cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@2@tmp/
				  git clone https://github.com/Thenmozhy/mnc_jenkinsfile.git 
				  cd mnc_jenkinsfile
				  ls -l
				  git branch --merged > commit
				  firstline=$(head -n1 commit)
				  echo "$firstline"
				  if [ "$firstline" == '* develop' ]
				  then
					echo "develop" > branch
				  else
					echo "master" > branch
				  fi
				  line=$(head -n1 branch)
				  echo "$line"
				  echo "finded latest merged branch"
                '''
			}
			catch (Exception e) {
			}
		  }				  
	    }
	  }  
  
    stage('clone_repo') {
	  steps {
	    echo "cloning repo"
	    script {
			try {
			    sh '''
			      #!/bin/bash
				  cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@2@tmp/
				  line=$(head -n1 branch)
				  echo "$line"
				  pwd
				  if [ "$line" == 'develop' ]
				  steps {
					checkout([
					$class: 'GitSCM',
					userRemoteConfigs: [[credentialsId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
					url: 'https://github.com/Thenmozhy/mnc_jenkinsfile/']]
					])
				  }
				  else
				    steps {
					  checkout([
					  $class: 'GitSCM',
					  userRemoteConfigs: [[credentialsId: '186d9d54-a7dd-46f3-867b-926dd7a6fba1',
					  url: 'https://github.com/Thenmozhy/mnc_jenkinsfile/']]
					  ])
				  }
				  fi				  
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
				  echo "$WORKSPACE"
				  cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV/
				  ls -l
                  zip -r "$WORKSPACE/REAN-ManagedCloud-repo.zip" /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV/branch -x *.git*
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
				  if [ $line == 'develop' ]; then
				    echo "Target branch is develop"
					aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://svc-rean-product-default-platform-artifacts/REAN-ManagedCloud-DEV/Develop/REAN-ManagedCloud-repo.zip
					echo "artifacts sent to develop"
					
				  else
					echo "Target branch is master"
					aws s3 cp $WORKSPACE/REAN-ManagedCloud-repo.zip s3://svc-rean-product-default-platform-artifacts/REAN-ManagedCloud-DEV/Master/REAN-ManagedCloud-repo.zip
					echo "artifacts sent to master"
				    exit 1
				  fi
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
