#! /usr/bin/env python
import os


def run(cmd, message=None):
    msg = message or cmd
    print("\n%s\n" % msg)
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Error running: %s" % msg)

travis_tag = os.getenv("TRAVIS_TAG")
travis_commmit = os.getenv("TRAVIS_COMMIT")
github_url = os.getenv("GITHUB_URL")
addon = os.getenv("ADDON")

docker_build = "docker run --rm --privileged --name {addon} " \
               "-v /var/run/docker.sock:/var/run/docker.sock " \
               "-v ~/.docker:/root/.docker " \
               "-v $(pwd):/docker " \
               "hassioaddons/build-env:latest " \
               "--login ${{DOCKER_USER}} " \
               "--password {{DOCKER_PASS}} " \
               "--author 'Daniel Manzaneque <danimanzaneque@gmail.com>' " \
               "--all"
if not travis_tag:
    docker_build = docker_build + " --test"
run(docker_build.format(addon=addon))
