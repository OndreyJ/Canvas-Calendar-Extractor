@echo off

call dependencies\Scripts\activate

python FetchCanvasCalendars.py

deactivate