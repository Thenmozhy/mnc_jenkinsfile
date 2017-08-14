pipeline {
  agent {
    node {
      label 'master'
      customWorkspace 'workspace/mncjenkinsfile-DEV/'
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
          git clone https://github.com/Thenmozhy/mnc_jenkinsfile.git
          cd mnc_jenkinsfile
          ls -l
          git pull
          git branch
          git checkout develop
          commit_dev=$(git rev-parse origin/develop)
          echo "$commit_dev"
          commit_mas=$(git rev-parse origin/master)
          echo "$commit_mas"
          lat_commit=$(git rev-list --remotes) > latest_commit
          branch_commit=$(head -n1 latest_commit)
          echo "$branch_commit"
          if [ "$branch_commit" == "$commit_mas" ]
          then
          echo "Commit on master branch"
          cd /var/lib/jenkins/workspace/mncjenkinsfile-DEV/mnc_jenkinsfile
          git checkout master
          zip -r master-branch.zip . -x ".*" -x "latest_commit" -x "*.zip"
          echo "master branch is zipped"
          aws s3 cp master-branch.zip s3://svc-rean-product-default-platform-artifacts/REAN-ManagedCloud-DEV/Master/master-branch.zip.zip
          echo "artitacts sent to s3"
          
          
          else
          echo "Commit on develop branch"
          cd /var/lib/jenkins/workspace/mncjenkinsfile-DEV/mnc_jenkinsfile
          git checkout develop
          zip -r develop-branch.zip . -x ".*" -x "latest_commit" -x "*.zip"
          ls -l
          echo "develop branch is zipped"
          aws s3 cp develop-branch.zip s3://svc-rean-product-default-platform-artifacts/REAN-ManagedCloud-DEV/Develop/develop-branch.zip.zip
          echo "artitacts sent to s3"
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
