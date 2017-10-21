#!/usr/bin/env groovy

node {
  stage('SCM') {
    git 'file:///development/python/poc'
  }
  stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
    def scannerHome = tool 'sqscanner';
    withSonarQubeEnv('SonarQube-local') {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
}