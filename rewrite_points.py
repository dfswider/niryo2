in_f = open("points_saved.txt", "r")
out_f = open("points1.txt", "a")

l = in_f.readlines()

for i in range(0, len(l), 2):
    out_f.write("source_points.append(PoseObject(" + l[i][:(len(l[i]))-1] + ", " + l[i+1][:(len(l[i+1]))-1] + "))\n")
out_f.write("\n")
for i in range(0, len(l), 2):
    out_f.write("upper_source_points.append(PoseObject(" + l[i][:(len(l[i]))-1] + ", " + l[i+1][:(len(l[i+1]))-1] + "))\n")