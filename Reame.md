# AI-Powered Software Development Workflow

This project implements an automated software development workflow using LangGraph and Google's Gemini AI. It simulates a complete software development lifecycle with AI agents playing different roles in the development process.

## Overview

The workflow orchestrates interactions between different AI agents, each representing a key role in the software development process:

- **Product Manager**: Converts requirements into structured user stories
- **Developer**: Implements features based on user stories
- **Reviewer**: Performs code reviews
- **Tester**: Conducts testing and quality assurance


### Workflow States

The workflow progresses through various states, managed by the `WorkflowState` class:

- Requirements
- User Story
- Implementation Code
- Review Feedback
- Test Results
- Validation Results

### State Transitions

1. **Product Manager** → **Developer**
   - Converts requirements to user stories

2. **Developer** → **Reviewer**
   - Implements the feature based on user story

3. **Reviewer** → **Tester** or **Developer**
   - Reviews code and either approves or requests changes

4. **Tester** → **Validator**
   - Runs tests and provides test results

5. **Validator** → **Done** or **Developer**
   - Validates if implementation meets requirements

## Key Features

- **Asynchronous Processing**: All agent operations are async for better performance
- **State Management**: Robust state handling using Pydantic models
- **Conditional Routing**: Dynamic workflow paths based on agent outputs
- **AI-Powered Decisions**: Uses Gemini AI for intelligent decision-making

## Technologies Used

- **LangGraph**: For workflow orchestration
- **Gemini AI**: For natural language processing and code generation
- **Pydantic**: For data validation and serialization
- **FastAPI** (implied from project structure): For API endpoints
