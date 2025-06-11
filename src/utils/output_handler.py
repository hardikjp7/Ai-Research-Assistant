import streamlit as st
import sys
from contextlib import contextmanager
from io import StringIO
import re


# output handler

class StreamlitProcessOutput:
    def __init__(self, container):
        self.container = container
        self.output_text = ""
        self.seen_lines = set()