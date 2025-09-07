# Sprint Management

This directory contains the sprint management system for the project.

## Structure

- `sprints.json` - Main data file containing all sprint information
- `sprint_manager.py` - Python script for querying and managing sprints

## Sprint Data Format

Each sprint contains the following fields:
- `id`: Unique identifier (e.g., "S_36")
- `name`: Display name (e.g., "S 36")
- `status`: Current status (planned, active, completed, cancelled)
- `created_date`: Date when sprint was created
- `start_date`: Sprint start date (null if not started)
- `end_date`: Sprint end date (null if not finished)
- `goals`: Array of sprint goals/objectives
- `tasks`: Array of tasks/stories in the sprint
- `description`: Sprint description

## Current Sprints

### S 36
- **Status**: Planned
- **Created**: 2024-09-07
- **Description**: Sprint S 36 - newly created sprint

## Usage

### Using the Sprint Manager Script

```bash
# List all sprints
python3 sprint_manager.py list

# Get specific sprint by ID
python3 sprint_manager.py get S_36
```

### Manual Editing

To add a new sprint, edit the `sprints.json` file and add a new sprint object to the `sprints` array. Remember to update the `metadata.total_sprints` count and `metadata.last_updated` date.