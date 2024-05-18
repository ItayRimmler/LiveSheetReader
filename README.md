# Music Sheet Page Turner

**VERSION 2 UNDER CONSTRUCTION! STAY PATIENT!**

## Table of Contents
1. [General Explanation](#general-explanation)
   - [Background](#background)
   - [Application](#application)
   - [History](#history)
   - [Thanks](#thanks)
2. [Project Structure](#project-structure)

---

## General Explanation

### Background
Hi! My name is Itay. This project was inspired by a conversation with my girlfriend's dad, a musician, who told me about a mechanical pedal pianists use to turn music sheet pages. I thought it was a bit silly because this process can be automated with today's technology. That's the goal of this project: to let a computer listen to the notes you play, compare them to the sheet music, and turn the page if you played correctly.

### Application
The project is divided into several tasks:
1. **Image Processing**: Recognizing notes from a well-scanned PDF file for each page.
2. **Audio Processing**: Identifying what you play using knowledge of how a note's FFT should appear.
3. **Chain Processing**: Creating a chain of notes from what the user has played and comparing it to the sheet music. A score is given based on the resemblance to the last bar. If there's resemblance to other bars, a lesser score is also given. If you score high enough, the program will turn the page.

### History
I've made several attempts at this project, learning a lot about Python and programming along the way. This version aims to be tidy and utilize existing algorithms, which is why you'll see other projects called "Sheet Reader" on my GitHub.

### Thanks
I'd like to thank my supportive family, my girlfriend, Yair (who gave me the idea), and anyone who offered advice and encouragement.

---

## Project Structure

```plaintext
data - Contains dictionaries needed to identify notes.

src - Contains:
    - app - Contains:
        - audio process - Scripts for processing audio.
        - chain process - Scripts for processing chains.
        - image process - Scripts for processing images.
        - pdf process - Scripts for processing PDF files.
        - all process - Scripts to assist with processing any of the above.
    - lib - Contains:
        - audio process - Libraries for processing audio.
        - chain process - Libraries for processing chains.
        - image process - Libraries for processing images.
        - pdf process - Libraries for processing PDF files.
        - all process - Libraries to assist with processing any of the above.

config - Contains:
    - audio config - Configuration for `src/app/audio process` and `src/lib/audio process`.
    - chain config - Configuration for `src/app/chain process` and `src/lib/chain process`.
    - image config - Configuration for `src/app/image process` and `src/lib/image process`.
    - all config - Configuration for `src/app/all process` and `src/lib/all process`.

docs - Contains documentation (except for the README).

temp - May contain temporary files during the run of the program.

assets - Contains PDF files to work with, and a diagram of how the program works.
