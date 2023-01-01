import projectGit

# calculator = projectGit.Calculator()
# calculator.interface_prompt()

c1 = projectGit.Coordinator(10, 20)
c2 = projectGit.Coordinator(20, 30)
c3 = c1 * c2
print(c3)
c3()
