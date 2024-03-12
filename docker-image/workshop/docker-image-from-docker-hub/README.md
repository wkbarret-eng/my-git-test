# 解答

## Docker images (before)
```bash=
$ sudo docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

## Docker search
```bash=
$ sudo docker search python
[sudo] password for ubuntu: 
NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
python                             Python is an interpreted, interactive, objec…   9489      [OK]       
hylang                             Hy is a Lisp dialect that translates express…   59        [OK]       
pypy                               PyPy is a fast, compliant alternative implem…   385       [OK]       
bitnami/python                     Bitnami Python Docker Image                     27                   [OK]
cimg/python                                                                        15                   
okteto/python                                                                      0                    
appdynamics/python-agent-init      AppDynamics Repository for Python agent inst…   0                    
rapidfort/python-chromedriver                                                      12                   
airbyte/python-connector-base                                                      0                    
intel/python                                                                       0                    
pachyderm/python-sdk-ci-testing                                                    0                    
pachyderm/python-build                                                             0                    
clearlinux/python                  Python programming interpreted language with…   9                    
faucet/python3                      Python3 docker image for amd64                 7                    
openwhisk/python3action            Apache OpenWhisk runtime for Python 3 Actions   6                    
openwhisk/python2action            Apache OpenWhisk runtime for Python v2 Actio…   2                    
mirantis/python-operations-api     https://mirantis.jira.com/browse/IT-40189       0                    [OK]
okteto/python-fastapi                                                              0                    
ubuntu/python                      A chiselled Ubuntu rock with the Python runt…   0                    
opensuse/python                    openSUSE base image with python                 0                    [OK]
submitty/python                    Official Repository for Submitty Python Imag…   0                    
fnndsc/python-poetry               Python Poetry                                   9                    
pipelinecomponents/python-safety   Safety by pyup.io for Python in a container …   0                    
pachyderm/python-evaluate                                                          0                    
openwhisk/python3aiaction          Apache OpenWhisk runtime for Python 3 Action…   2                    
```

## Docker pull
```bash=
$ sudo docker pull python
Using default tag: latest
latest: Pulling from library/python
71215d55680c: Pull complete 
3cb8f9c23302: Pull complete 
5f899db30843: Pull complete 
567db630df8d: Pull complete 
d68cd2123173: Pull complete 
63941d09e532: Pull complete 
097431623722: Pull complete 
09527fa4de8d: Pull complete 
Digest: sha256:fcb0f566de12e4585c8a80a2390337baa51c197f7639eb969eb82b36212ddae3
Status: Downloaded newer image for python:latest
docker.io/library/python:latest
```
## Docker images (after)
```bash=
$ sudo docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
python       latest    ae29c48b7429   4 weeks ago   1.02GB
```

## Run
```bash=
$ sudo docker run -ti python
Python 3.12.2 (main, Mar 12 2024, 11:02:14) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
