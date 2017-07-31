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
				  cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/
				  git clone https://github.com/Thenmozhy/mnc_jenkinsfile.git 
				  cd mnc_jenkinsfile
				  ls -l
				  commit=$(git rev-parse origin/master)
				  git check develop
				  git checkout master
				  echo "$commit"
				  cd .git/refs/heads
				  master_commit=$(head -n1 master)
				  echo "$master_commit"
				  dev_commit=$(head -n1 develop)
				  echo "$dev_commit"
				  if [ "$commit" == "$master_commit" ]
				  
				  
				  then
					echo "Commit on master branch"
					cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/mnc_jenkinsfile
					git checkout master
					zip -r "/var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/mnc_jenkinsfile/REAN-ManagedCloud-repo.zip" /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/mnc_jenkinsfile -x *.git* 
					
				  else
					echo "Commit on develop branch"
					cd /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/
					git checkout develop
					zip -r "/var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/mnc_jenkinsfile/REAN-ManagedCloud-repo.zip" /var/lib/jenkins/workspace/REAN-ManagedCloud-DEV@tmp/mnc_jenkinsfile -x *.git*
					
				  fi
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
				  commit=$(git rev-parse origin/master)
				  echo "$commit"
				  cd .git/refs/heads
				  master_commit=$(head -n1 master)
				  echo "$master_commit"
				  dev_commit=$(head -n1 develop)
				  echo "$dev_commit"
				  if [ "$commit" == "$master_commit" ]
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
