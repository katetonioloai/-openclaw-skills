#!/bin/bash
# create_voice_agent.sh — Create a GHL AI Voice Agent via API
# Usage: bash create_voice_agent.sh --name "..." --business "..." --greeting "..." --prompt "..."
# Optional: --phone "+1941..." --voice "voiceId" --duration 300

set -e

GHL_API_TOKEN=$(grep '^GHL_API_TOKEN=' ~/.secrets/agents.env | cut -d= -f2- | tr -d '"' | tr -d "'")
GHL_LOCATION_ID=$(grep '^GHL_LOCATION_ID=' ~/.secrets/agents.env | cut -d= -f2- | tr -d '"' | tr -d "'")

NAME=""
BUSINESS=""
GREETING=""
PROMPT=""
PHONE=""
VOICE_ID="uYXf8XasLslADfZ2MB4u"  # Default: Nina (warm female)
DURATION=300

while [[ $# -gt 0 ]]; do
  case "$1" in
    --name)     NAME="$2";     shift 2 ;;
    --business) BUSINESS="$2"; shift 2 ;;
    --greeting) GREETING="$2"; shift 2 ;;
    --prompt)   PROMPT="$2";   shift 2 ;;
    --phone)    PHONE="$2";    shift 2 ;;
    --voice)    VOICE_ID="$2"; shift 2 ;;
    --duration) DURATION="$2"; shift 2 ;;
    *) echo "Unknown flag: $1"; exit 1 ;;
  esac
done

if [[ -z "$NAME" || -z "$BUSINESS" || -z "$GREETING" || -z "$PROMPT" ]]; then
  echo "ERROR: --name, --business, --greeting, and --prompt are all required."
  exit 1
fi

# Build JSON payload
PAYLOAD=$(python3 -c "
import json, sys
data = {
  'locationId': '$GHL_LOCATION_ID',
  'agentName': $(python3 -c "import json; print(json.dumps('$NAME'))"),
  'businessName': $(python3 -c "import json; print(json.dumps('$BUSINESS'))"),
  'welcomeMessage': $(python3 -c "import json; print(json.dumps('$GREETING'))"),
  'agentPrompt': $(python3 -c "import json; print(json.dumps('$PROMPT'))"),
  'language': 'en-US',
  'timezone': 'US/Eastern',
  'maxCallDuration': $DURATION,
  'responsiveness': 1,
  'voiceId': '$VOICE_ID'
}
if '$PHONE':
  data['inboundNumbers'] = ['$PHONE']
print(json.dumps(data))
")

RESPONSE=$(curl -s -X POST "https://services.leadconnectorhq.com/voice-ai/agents" \
  -H "Authorization: Bearer $GHL_API_TOKEN" \
  -H "Version: 2021-04-15" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

AGENT_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('agent',{}).get('id','') or d.get('id',''))" 2>/dev/null)

if [[ -z "$AGENT_ID" ]]; then
  echo "ERROR: Agent creation failed."
  echo "$RESPONSE"
  exit 1
fi

echo "✅ Voice agent created successfully!"
echo "Agent ID:   $AGENT_ID"
echo "Agent Name: $NAME"
echo "Business:   $BUSINESS"
[[ -n "$PHONE" ]] && echo "Phone:      $PHONE" || echo "Phone:      (none assigned)"
echo ""
echo "Full response:"
echo "$RESPONSE" | python3 -m json.tool
