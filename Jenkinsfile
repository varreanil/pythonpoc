#!/usr/bin/env groovy

node {
  stage('SCM') {
    git 'file:///development/python/poc'
  }
  stage('SonarQube analysis') {
    echo "Anil::: $WORKSPACE"
    sh "ls $WORKSPACE/apiutils"
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'sqscanner';
    withSonarQubeEnv('SonarQube-local') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}