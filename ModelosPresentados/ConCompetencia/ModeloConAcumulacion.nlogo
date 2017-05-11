extensions [csv array]
globals[pubtotal total-energy actual-papers total-distance-mean att-file probability acumulated-papers pubUniversities probUniversities probIncreaseUniversities]
turtles-own [
  university
  energy
  pub
  mov
  prob
  ]
patches-own [papers]


to-report get-att
  report (list who pub university)
end

to export
  file-open (word prueba "/" numberGroupsUniversity1 "-" numberGroupsUniversity2 "-" numberGroupsUniversity3  "-" numberGroupsUniversity4 "-" numberGroupsUniversity5 "-" numberGroupsUniversity6 "-" initial-probability-agents "-" probabilityIncrease1 "-" probabilityIncrease2 "-" probabilityIncrease3 "-" probabilityIncrease4 "-" probabilityIncrease5 "-" probabilityIncrease6 "-" initial-energy "-turtles.csv")
  ask turtles [
    file-print csv:to-row get-att
  ]
  file-close
  export-all-plots (word prueba "/" numberGroupsUniversity1 "-" numberGroupsUniversity2 "-" numberGroupsUniversity3  "-" numberGroupsUniversity4 "-" numberGroupsUniversity5 "-" numberGroupsUniversity6 "-" initial-probability-agents "-" probabilityIncrease1 "-" probabilityIncrease2 "-" probabilityIncrease3 "-" probabilityIncrease4 "-" probabilityIncrease5 "-" probabilityIncrease6 "-" initial-energy "-curve.csv")
end


to setup
clear-all
setup-turtles
reset-ticks
end



to setup-turtles
create-turtles numberGroupsUniversity1 [set university 0]
create-turtles numberGroupsUniversity2 [set university 1]
create-turtles numberGroupsUniversity3 [set university 2]
create-turtles numberGroupsUniversity4 [set university 3]
create-turtles numberGroupsUniversity5 [set university 4]
create-turtles numberGroupsUniversity6 [set university 5]
set pubUniversities array:from-list n-values universities [0]
set probUniversities array:from-list n-values universities [initial-probability-agents]
set probIncreaseUniversities array:from-list n-values universities [0]
array:set probIncreaseUniversities 0 probabilityIncrease1
array:set probIncreaseUniversities 1 probabilityIncrease2
array:set probIncreaseUniversities 2 probabilityIncrease3
array:set probIncreaseUniversities 3 probabilityIncrease4
array:set probIncreaseUniversities 4 probabilityIncrease5
array:set probIncreaseUniversities 5 probabilityIncrease6

ask turtles [
  setxy random-xcor random-ycor
  set energy initial-energy
  set total-energy energy * count turtles
  set mov 1
   ]

grow-papers
end




to go
  if total-energy = 0 or ticks > 2000[ file-close export stop ] ;;
  move-turtles
  energize

  tick;; increase the tick counter by 1 each time throughend
end

to move-turtles
  ask turtles [
    ifelse energy > 0[
    right random 360
    forward mov
    set energy energy - 1
    set total-energy total-energy - 1
    ]
    [
     set color black
    ]
  ]
end


to energize
ask turtles [

  if energy > 0 [
    if papers > 0 [
      set papers papers - 1
      set actual-papers actual-papers - 1
      if random-float 1 < (array:item probUniversities university)[
        array:set pubUniversities university ((array:item pubUniversities university) + 1)
        set pub pub + 1
        set energy energy + 1
        set total-energy total-energy + 1
        if ((array:item probUniversities university) + (array:item probIncreaseUniversities university)) < 100 [
          array:set probUniversities university ((array:item probUniversities university) + (array:item probIncreaseUniversities university))
        ]
        set pcolor black
      ]
    ]
  ]
]
end





to grow-papers
ask patches [
      set papers papers + 1
      set acumulated-papers acumulated-papers + 1
      set actual-papers actual-papers + 1
]
end
@#$#@#$#@
GRAPHICS-WINDOW
587
45
832
177
-1
-1
1.008
1
1
1
1
1
0
1
1
1
0
1000
0
1000
1
1
1
ticks
30.0

BUTTON
5
10
116
43
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
120
10
183
43
NIL
go
T
1
T
OBSERVER
NIL
NIL
NIL
NIL
0

PLOT
2
347
162
467
pubUniversity0
time
totals
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"turtles" 1.0 0 -16777216 true "" "plot array:item pubUniversities 0"

BUTTON
117
51
186
84
export
export
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

PLOT
181
10
341
130
Energy
time
total
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot total-energy"

PLOT
236
235
396
355
Agents-with-energy
time
total
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot count turtles with [energy > 0]"

INPUTBOX
401
238
486
298
prueba
test0
1
0
String

SLIDER
-5
236
117
269
probabilityIncrease1
probabilityIncrease1
0
1
0
0.001
1
NIL
HORIZONTAL

SLIDER
3
199
95
232
numberGroupsUniversity1
numberGroupsUniversity1
0
1000
1000
1
1
NIL
HORIZONTAL

PLOT
163
347
323
467
probabilityUniversity0
total
time
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 0"

PLOT
325
466
485
586
acumulated-papers
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot acumulated-papers"

PLOT
324
349
484
469
actual-papers
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot actual-papers"

SLIDER
1
159
173
192
universities
universities
0
10
0
1
1
NIL
HORIZONTAL

PLOT
0
473
160
593
pubUniversity1
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item pubUniversities 1"

PLOT
163
468
323
588
probabilityUniversity1
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 1"

SLIDER
-12
271
117
304
probabilityIncrease2
probabilityIncrease2
0
1
0
1
1
NIL
HORIZONTAL

SLIDER
-7
304
118
337
probabilityIncrease3
probabilityIncrease3
0
1
1.0E-4
1
1
NIL
HORIZONTAL

PLOT
2
588
162
708
pubUniversity2
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item pubUniversities 2"

PLOT
164
590
324
710
probabilityUniversity2
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 2"

SLIDER
301
162
418
195
numberGroupsUniversity2
numberGroupsUniversity2
0
10000
997
1
1
NIL
HORIZONTAL

SLIDER
186
163
300
196
numberGroupsUniversity3
numberGroupsUniversity3
0
10000
1000
1
1
NIL
HORIZONTAL

SLIDER
4
86
104
119
initial-probability-agents
initial-probability-agents
0
100
1
1
1
NIL
HORIZONTAL

SLIDER
0
124
156
157
initial-energy
initial-energy
0
1000
100
1
1
NIL
HORIZONTAL

SLIDER
95
198
187
231
numberGroupsUniversity4
numberGroupsUniversity4
0
1000
50
1
1
NIL
HORIZONTAL

SLIDER
186
200
302
233
numberGroupsUniversity5
numberGroupsUniversity5
0
1000
53
1
1
NIL
HORIZONTAL

SLIDER
300
199
414
232
numberGroupsUniversity6
numberGroupsUniversity6
0
1000
56
1
1
NIL
HORIZONTAL

SLIDER
120
235
238
268
probabilityIncrease4
probabilityIncrease4
0
1
0.1
1
1
NIL
HORIZONTAL

SLIDER
120
269
237
302
probabilityIncrease5
probabilityIncrease5
0
1
0.1
1
1
NIL
HORIZONTAL

SLIDER
121
305
239
338
probabilityIncrease6
probabilityIncrease6
0
1
0.1
1
1
NIL
HORIZONTAL

PLOT
3
708
163
828
pubUniversity3
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item pubUniversities 3"

PLOT
3
829
163
949
pubUniversity4
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item pubUniversities 4"

PLOT
3
948
163
1068
pubUniversity5
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item pubUniversities 5"

PLOT
163
708
323
828
probabilityUniversity3
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 3"

PLOT
163
827
323
947
probabilityUniversity4
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 4"

PLOT
163
948
323
1068
probabilityUniversity5
NIL
NIL
0.0
10.0
0.0
10.0
true
false
"" ""
PENS
"default" 1.0 0 -16777216 true "" "plot array:item probUniversities 5"

@#$#@#$#@
## WHAT IS IT?

(a general understanding of what the model is trying to show or explain)

## HOW IT WORKS

(what rules the agents use to create the overall behavior of the model)

## HOW TO USE IT

(how to use the model, including a description of each of the items in the Interface tab)

## THINGS TO NOTICE

(suggested things for the user to notice while running the model)

## THINGS TO TRY

(suggested things for the user to try to do (move sliders, switches, etc.) with the model)

## EXTENDING THE MODEL

(suggested things to add or change in the Code tab to make the model more complicated, detailed, accurate, etc.)

## NETLOGO FEATURES

(interesting or unusual features of NetLogo that the model uses, particularly in the Code tab; or where workarounds were needed for missing features)

## RELATED MODELS

(models in the NetLogo Models Library and elsewhere which are of related interest)

## CREDITS AND REFERENCES

(a reference to the model's URL on the web if it has one, as well as any other necessary credits, citations, and links)
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270

@#$#@#$#@
NetLogo 5.2.1
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
<experiments>
  <experiment name="bastantesAgentes" repetitions="1" runMetricsEveryStep="true">
    <setup>setup</setup>
    <go>go</go>
    <timeLimit steps="2002"/>
    <enumeratedValueSet variable="numberGroupsUniversity1">
      <value value="100"/>
      <value value="1000"/>
      <value value="10000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity2">
      <value value="100"/>
      <value value="1000"/>
      <value value="10000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity3">
      <value value="100"/>
      <value value="1000"/>
      <value value="10000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="initial-probability">
      <value value="0.01"/>
      <value value="0.1"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease1">
      <value value="0.01"/>
      <value value="1.0E-4"/>
      <value value="1.0E-6"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease2">
      <value value="0.01"/>
      <value value="1.0E-4"/>
      <value value="1.0E-6"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease3">
      <value value="0.01"/>
      <value value="1.0E-4"/>
      <value value="1.0E-6"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="universities">
      <value value="3"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="initial-probability-agents">
      <value value="0.01"/>
      <value value="1.0E-4"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="initial-energy">
      <value value="100"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="prueba">
      <value value="&quot;test2&quot;"/>
    </enumeratedValueSet>
  </experiment>
  <experiment name="testIndividual" repetitions="1" runMetricsEveryStep="true">
    <setup>setup</setup>
    <go>go</go>
    <timeLimit steps="2002"/>
    <enumeratedValueSet variable="numberGroupsUniversity1">
      <value value="1000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity2">
      <value value="1000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity3">
      <value value="1000"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity4">
      <value value="100"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity5">
      <value value="100"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="numberGroupsUniversity6">
      <value value="100"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease1">
      <value value="0.001"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease2">
      <value value="1.0E-4"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease3">
      <value value="1.0E-5"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease4">
      <value value="0.01"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease5">
      <value value="0.001"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="probabilityIncrease6">
      <value value="1.0E-4"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="universities">
      <value value="6"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="initial-probability-agents">
      <value value="0.001"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="initial-energy">
      <value value="100"/>
    </enumeratedValueSet>
    <enumeratedValueSet variable="prueba">
      <value value="&quot;test0&quot;"/>
    </enumeratedValueSet>
  </experiment>
</experiments>
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180

@#$#@#$#@
0
@#$#@#$#@
