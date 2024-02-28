This file has two purposes:
1. It'll generally explain the project
2. It'll give the table of contents for the project's structure

1. General explanation for the project:

BACKGROUND: My name is Itay. One day, I sat with my girlfriend's dad, a musician, and he told me about a pedal that pianists use to move a page in a music sheet, mechanically. I thought 
that's kinda silly, because it can be easily automated: with today's processing power and technology, it's obvious even to a mere student such as I, that you can let a computer listen to
the notes that you play, then compare it to the sheet, and finally compare the two to see if you played correctly. This is what the project is going to attempt to do.

APPLICATION: I'm going to divide this into several tasks - a. Image processing: recognizing from a well scanned pdf file notes, for each page in the file. b. Audio processing: recognizing
what you play and identify it, using my knowledge of how a note's FFT should be seen. c. Chain processing: I create a chain from whatever the user has played (chain is a group of specific
notes with a specific order), and I compare it to a chain, or a combination of chains, from the sheet. We give a score based on the resemblence to the last bar. If there's a resemblence to
other bars, we also give it lesser score. If you score high enough, the program will turn a page.

HISTORY: I can say a lot here, but I don't feel like writing too much, I'm too busy and I'm not a storywriter. I will say that I made several attempts, and they taught me a lot about python
and programming in general. I decided to make another one, and this time, keep my code tidy, and use already existing algorithms. That's why you might see in my Github page other projects
that are called "Sheet Reader".

THANKS: I'd like to thank my supportive family, my girlfriend, Yair - who gave me the idea, and anyone who gave me advices along the way and convinced me to do this project and use python.


2. Table of Contents for the project's structure:

data - contains the dictionaries that we need to identify notes.

src - contains:
		- app - contains:
				- audio process - contains scripts that process audio
				- chain process - contains scripts that process chains
				- image process - contains scripts that process images
				- pdf process - contains scripts that process pdf files
				- all process - contains scripts that help us process any of the above
		- lib - contains:
				- audio process - contains libraries that process audio
				- chain process - contains libraries that process chains
				- image process - contains libraries that process images
				- pdf process - contains libraries that process pdf files
				- all process - contains libraries that help us process any of the above

config - contains:
	- audio config - contains configuration (constants, parameters, etc.) for the src\app\audio process and src\lib\audio process
	- chain config - contains configuration (constants, parameters, etc.) for the src\app\chain process and src\lib\chain process
	- image config - contains configuration (constants, parameters, etc.) for the src\app\image process and src\lib\image process
	- all config - contains configuration (constants, parameters, etc.) for the src\app\all process and src\lib\all process

docs - contains documentations, except for the README.

