# attentionalBlink
Experiment demonstrating a cognitive psychological phenomenon called attentional blink.

The study was developed in PsychoPy v2020.2.10 with python 3.6.6.

In each trial, the participant observes a stream of 20 letters presented at the center of the screen. Each letter is presnted for 2 frames each separated by a 4 frame blank screen. Every stream contains a single white letter (T1) amongst black letters. In half of the trials the letter X (T2) is presented somewhere after the white letter with a lag of 1,3,5 or 7 letters. After observing the stream, participants answer an identity question and a detection question. 
Identity question: What letter was presented in white?
Detection question: Did you see an X in the stream?

Typical finding is that detection accuracy for T2 drops on trials with a lag of 3, compared to trials with a lag of 5-7 letters. That is, T2 detection fails if T2 follows T1 within a 200-500 ms time window. 

The phenomenon reflects the temporal costs in allocating selective attention.
