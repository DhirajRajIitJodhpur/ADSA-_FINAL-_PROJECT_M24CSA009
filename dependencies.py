import networkx as nx
from flask import Flask, request, jsonify, render_template
import requests
import sys
import io
import webbrowser

app = Flask(__name__)

STACK_OVERFLOW_API_URL = 'https://api.stackexchange.com/2.3/search'