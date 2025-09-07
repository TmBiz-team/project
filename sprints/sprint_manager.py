#!/usr/bin/env python3
"""
Simple sprint management script for querying sprint information.
"""

import json
import os
import sys

def load_sprints():
    """Load sprints from JSON file."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sprints_file = os.path.join(script_dir, 'sprints.json')
    
    try:
        with open(sprints_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {sprints_file} not found")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {sprints_file}")
        sys.exit(1)

def list_sprints():
    """List all sprints."""
    data = load_sprints()
    sprints = data.get('sprints', [])
    
    if not sprints:
        print("No sprints found.")
        return
    
    print("Available Sprints:")
    print("-" * 50)
    for sprint in sprints:
        print(f"ID: {sprint['id']}")
        print(f"Name: {sprint['name']}")
        print(f"Status: {sprint['status']}")
        print(f"Created: {sprint['created_date']}")
        print(f"Description: {sprint['description']}")
        print("-" * 50)

def get_sprint(sprint_id):
    """Get specific sprint by ID."""
    data = load_sprints()
    sprints = data.get('sprints', [])
    
    for sprint in sprints:
        if sprint['id'] == sprint_id:
            return sprint
    return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "list":
            list_sprints()
        elif command == "get" and len(sys.argv) > 2:
            sprint_id = sys.argv[2]
            sprint = get_sprint(sprint_id)
            if sprint:
                print(json.dumps(sprint, indent=2))
            else:
                print(f"Sprint '{sprint_id}' not found")
        else:
            print("Usage: python3 sprint_manager.py [list|get <sprint_id>]")
    else:
        print("Sprint Management System")
        print("Usage: python3 sprint_manager.py [list|get <sprint_id>]")
        print("\nCommands:")
        print("  list          - List all sprints")
        print("  get <id>      - Get specific sprint by ID")