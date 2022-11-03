pipeline{
agent any
tools {
maven 'Maven'
}
stages{
stage("Git Clone"){
steps
{
git 'https://github.com/Parag3009/hello-world.git'
}
}
stage("Build"){
steps
{
bat 'mvn clean install'
}
}
stage("Deploy"){
steps
{
bat 'copy  C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\120a3009_pipe\\webapp\\target\\webapp.war E:\\apache-tomcat-9.0.65\\webapps'
}
}
}
}
