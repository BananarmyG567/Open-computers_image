local Serial = require("serialization")
local component = require("component")
local os = require("os")
local computer = require("computer")
local gpu = component.gpu

if computer.getArchitecture and computer.getArchitecture() == "Lua 5.2" then
    print("Wrong Lua version(take cpu out and crouch right click to switch it to lua 5.3)")
    os.exit()
else
    local func, _ = load("return function(r,g,b) return r<<16|g<<8|b end")
    _, RGBToInteger = pcall(func)
end

local arguments_as_a_table = {...}

if arguments_as_a_table[1] == nil then 
    print("Error: please give file path")
end

F = io.open(arguments_as_a_table[1],"r")
outS = Serial.unserialize(F:read())
F:close()

V1 = 2
T1 = {0,0,0}

for y = 1, outS[1][2], 1 do

    for x = 1, outS[1][1], 1 do

        if outS[V1] ~= T1 then
            gpu.setForeground(RGBToInteger(outS[V1][1],outS[V1][2],outS[V1][3]))
            gpu.setBackground(RGBToInteger(outS[V1][1],outS[V1][2],outS[V1][3]))
            gpu.fill(x,y,1,1," ")

        end
        V1 = V1 + 1

    end
end