# Campaign Management System

A utility for managing JIRA campaign data and converting between various formats.

## Tools

### json2csv

Converts a JSON file with campaign information to CSV format.

**Usage:**
```bash
fps json2csv.py json2csv.fps
```

**Configuration:**
Edit `json2csv.fps` to set input/output file paths.

## File Format

The input JSON file should contain campaign information in the format:
```json
{
  "Campaign1": {
    "go": true,
    ...
  },
  "Campaign2": {
    "go": false,
    ...
  }
}
```

The output CSV will have the format:
```
Campaign,Status
Campaign1,enabled
Campaign2,present
```

## License

MIT 