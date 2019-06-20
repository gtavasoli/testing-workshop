# Testing Workshop

Application testing methods workshop material. 

[![Website gtavasoli.blog.ir](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://gtavasoli.blog.ir/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://t.me/gtavasoli_me)

## Table of Contents
- [Topics covered](#topics-covered)
- [System Requirements](#system-requirements)
- [Setup](#setup)
- [Workshop Plan](#workshop-plan)
- [LICENSE](#licence)


## Topics covered
1. Unit Testing with [unittest](https://docs.python.org/3/library/unittest.html)
2. Mocking
3. Performance Test

## System Requirements
- [git][git] v2.14.1 or greater
- [python3][python3] v3.x
- [jre-8][jre-8] or greater (To Run JMeter in Development Environment)

All of these must be available in your PATH. To verify things are set up properly, you can run this:

```
git --version
python --version
java --version (development env.)
```

## Setup
After you've made sure to have the correct things (and versions) installed, you should be able to just run a few commands to get set up:

```
git clone https://github.com/gtavasoli/testing-workshop.git
cd testing-workshop
```

## Workshop Plan
- Introduction [[slides]]
- Unit Testing
  - Calculator Sample
  - Employee Sample
  - Flaskr
- Mocking
   - Random person sample
  - Employee Sample
  - Error sample
- TDD – Test Driven Development
- Performance Test
  - JMeter Intro
    - Sample 1 - Simple test
    - Sample 2 - Using assertions
  - Flaskr
    - Parametric requests
    - Single Thread (with or without wait)
    - Multi Thread (GIL)
    - NGINX + uWSGI (worker)
  - JMeter plugins 
  - Profiling


## LICENSE
All of the codebase are MIT licensed unless otherwise specified. 

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

[git]: https://git-scm.com/
[python3]: https://www.python.org/downloads/release/python-373/
[jre-8]: https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html
[slides]: http://
[flaskr]: https://github.com/pallets/flask/tree/master/examples/tutorial/flaskr