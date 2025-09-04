-- Inspired by the random number generator on the CASIO FX-9860 GIII "ay bro you got your calc? :P"
-- By SunnyFlops, written in like an hour lol

-- generator settings
local matches = 3
local min = 1
local max = 40
local nums = 6

-- variables
local hasSetup = false

math.randomseed(os.time())

local counter = 0

-- user inputs
local function setup()
    print("[6 ] numbers:")
    nums = io.read()

    print("[1 ] min:")
    min = io.read()

    print("[40] max:")
    max = io.read()

    print("[3 ] matches:")
    matches = io.read()

    -- i would add error handling but why should i
    nums = tonumber(nums)
    min = tonumber(min)
    max = tonumber(max)
    matches = tonumber(matches)

    hasSetup = true
end

-- actual randomiser
local function randomise()
    counter = counter + 1
    local returnList = {}

    for i = 1, nums do
        returnList[i] = math.random(min, max)
    end

    print(counter .. " --- " .. table.concat(returnList, ", "))

    return returnList
end

local function counted(numbers)
    local counts = {}
    for _, v in ipairs(numbers) do
        counts[v] = (counts[v] or 0) + 1
    end
    return counts
end

-- main function
while true do
    if not hasSetup then
        setup()
    end

    local numbers = randomise()
    local counts = counted(numbers)

    for _, v in pairs(counts) do
        if v >= matches then
            print("WOW! " .. matches .. " of em!!!! Achieved in " .. counter .. " turns")
            os.exit(_, _)
        end
    end
end