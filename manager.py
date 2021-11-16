import os
from sys import exit

run_scripts = {
    "javascript": ["node nodejs.js"],
    "java": ["javac JavaApp.java", "java JavaApp"],
    "lua": ["lua lua.lua"],
    "storyscript": ["cd resources", "cd StoryScript", "python -m storyscript -i ../../storyscript.sts", "cd ..", "cd .."],
    "rust": ["rustc rust.rs --out-dir bin", "./bin/rust"],
    "ruby": ["ruby ruby.rb"],
    "cpp": ["g++ cpp.cpp -o bin/cpp", "./bin/cpp"],
    "c": ["g++ c.c -o bin/c", "./bin/c"],
    "d": ["gdc d.d -o bin/d", "./bin/d"],
    "dart": ["dart dart.dart"],
    "ocaml": ["ocaml ocaml.ml"],
    "perl": ["perl perl.pl"],
    "python": ["python python.py"],
    "neo": ["java -jar resources/Neo.jar neo.neo"],
    "go": ["go run golang.go"],
    "swift": ["swift swift.swift"]
}

target_script = run_scripts.get(input("Please enter the script you wanted to run > "))

if target_script is None:
    print("Target script is not defined. Exiting...")
    exit(1)

for i in target_script:
    os.system(i)

