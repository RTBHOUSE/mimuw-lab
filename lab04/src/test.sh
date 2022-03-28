#!/bin/bash

curl -v -X POST -H 'content-type: text/plain' -d @test_source.cpp http://localhost:5000/tasks/sort/score
