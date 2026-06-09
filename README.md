# Backup Verification Simulator

## AI-Powered Backup Integrity Validation and Failure Analysis System

### Project Overview

Backup Verification Simulator is an AI-assisted data integrity verification system that validates backup files against original datasets and identifies backup failures through automated verification checks.

The system simulates a real-world backup verification workflow by comparing an original dataset with its backup copy and performing multiple validation checks such as:

* Row Count Verification
* Missing Row Detection
* Duplicate Record Detection
* Schema Validation
* Checksum Verification

When validation issues are detected, the AI module analyzes the failure and generates human-readable explanations, root cause analysis, and corrective recommendations.

The project demonstrates how AI can be integrated into backup verification workflows to improve reliability, reduce manual effort, and provide actionable insights for data recovery and maintenance.

---

## Problem Statement

Organizations rely on backup systems to protect critical business data. However, backup files may become incomplete, corrupted, duplicated, or structurally inconsistent due to failures during the backup process.

Manually identifying these issues can be time-consuming and error-prone.

Backup Verification Simulator automates the verification process by validating backup integrity and providing intelligent analysis of detected issues through AI-generated explanations and reports.

---

## Key Features

### Data Integrity Verification

* Row Count Validation
* Missing Row Detection
* Duplicate Record Detection
* Schema Validation
* Checksum Verification

### AI-Powered Analysis

* Failure Explanation
* Root Cause Analysis
* Recovery Recommendations
* Automated Report Generation

### Agent-Based Workflow

* Validation Orchestration
* Decision-Based AI Invocation
* Report Generation Pipeline

### Interactive User Interface

* CSV File Upload
* PASS / FAIL Status Display
* Validation Metrics Dashboard
* AI Analysis Visualization
* Verification Report Viewer

---

## Technology Stack

### Backend

* Python

### Data Processing

* Pandas

### AI Integration

* Google Gemini API

### Frontend

* Streamlit

### Version Control

* Git
* GitHub

---

## Project Goal

The primary goal of this project is to simulate an intelligent backup verification system capable of detecting backup inconsistencies and providing automated analysis that helps users quickly understand and resolve backup-related issues.

The system combines traditional data validation techniques with AI-generated explanations to create a practical and user-friendly backup verification solution.

##  Setup Instructions 

git clone ...
cd Backup-Verification-Simulator

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

env

GEMINI_API_KEY=YOUR_API_KEY

## Run Instructions 

streamlit run ui/app.py

Upload:

original.csv
backup_good.csv

or

original.csv
backup_bad.csv

## Architecture

User
 ↓
Streamlit UI
 ↓
Validation Engine
 ↓
Agent Workflow
 ↓
Decision Engine
 ↓
AI Analysis
 ↓
Report Generator
 ↓
Dashboard
 

 ## Assmptions

 1. Input files are CSV.
2. Original dataset is source of truth.
3. Users upload valid CSV files.
4. Internet available for Gemini API.

## limitations

1. CSV files only.
2. Large files may take longer.
3. Gemini API quota limitations.
4. Depends on AI service availability.
5. Proof-of-concept implementation.

