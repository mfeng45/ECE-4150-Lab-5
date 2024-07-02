# Lab 5: Batch Data Analysis using Hadoop, MapReduce, Pig, and Hive
=====================================================

## Overview

In this lab, you will learn how to set up a Hadoop cluster and run MapReduce, Pig, and Hive jobs.

## Setup Steps

### 1. Set up a Hadoop Cluster with EMR

### 2. Edit the Inbound Rules and Add a Rule for SSH

### 3. Connect to the Master Node using SSH

### 4. Upload Datasets to HDFS

### 5. Enable an SSH Tunnel to the EMR Master Node

### 6. Install SwitchyOmega in Chrome

### 7. Create Map Reduce Files in the Hadoop Master Node using Vim

### 8. Set up MrJob on Master Node

### 9. Run MapReduce Program

### 10. Run Pig Program (2 Ways)

#### Approach 1: Using EMR Steps

#### Approach 2: Using Terminal

## Challenges

### 1. Implement a MapReduce Program to Emit Bigrams Coined After 1992

Output: `(bigram, year)`

Example: `(mobile phone, 1996)`

### 2. Implement a MapReduce Program to Emit Average Bigram Frequency

Output: `(bigram, average)`

Example: `(how are, 6)`

### 3. Implement a Pig Program to Compute Most Common Bigram in 2003

Output: `(bigram, count)`

Example: `(how many, 5001)`

### 4. Implement a Pig Program to Compute Most Common Bigram in Each Year

Output: `(year, bigram, count)`

Example: `(2003, mobile phone, 3012)`

### 5. Create a Hive Meta-Store Table and Implement a Hive Query to Find Most Popular Bigram

Implement a Hive query to find the most popular bigram (over all the years) using the SQL-like Hive Query Language.
