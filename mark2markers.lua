-- Marker settings
START_OFFSET_SECONDS = 15
MARKER_DURATION_SECONDS = 15

-- Get Resolve
resolve = Resolve()
pm = resolve:GetProjectManager()
project = pm:GetCurrentProject()
timeline = project:GetCurrentTimeline()

if not timeline then
    print("No active timeline.")
    return
end

fps = tonumber(project:GetSetting("timelineFrameRate"))

function secondsToFrames(seconds)
    return math.floor(seconds * fps + 0.5)
end

-- File picker
fusion = resolve:Fusion()
filepath = fusion:RequestFile("", "", {["File Types"] = "Mark Files (*.mark)|*.mark"})

if not filepath or filepath == "" then
    print("No file selected.")
    return
end

-- Read file
file = io.open(filepath, "r")
if not file then
    print("Could not open file.")
    return
end

content = file:read("*all")
file:close()

-- Basic JSON parsing using Lua pattern matching
-- Works for your simple format
markersAdded = 0

for typeVal, timeVal in string.gmatch(content, '"type"%s*:%s*"([^"]+)".-"time"%s*:%s*([%d%.]+)') do

    if typeVal ~= "start" then

        eventTime = tonumber(timeVal)

        markerStartSeconds = math.max(0, eventTime - START_OFFSET_SECONDS)

        startFrame = secondsToFrames(markerStartSeconds)
        durationFrames = secondsToFrames(MARKER_DURATION_SECONDS)

        timeline:AddMarker(
            startFrame,
            "Blue",
            typeVal,
            "",
            durationFrames
        )

        markersAdded = markersAdded + 1
    end
end

print("Added " .. markersAdded .. " markers.")