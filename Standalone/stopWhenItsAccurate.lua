local spaces = ""

while true do
    print("[" .. spaces .. "]")

    spaces = spaces .. " "

    os.execute("sleep " .. tonumber(0.2))
end
