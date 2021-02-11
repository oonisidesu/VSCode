S = input()

# if S.count(S[0]) == 2:
#     if S[0] != S[1]:
#         if S.count(S[1]) == 2:
#             print("Yes")
#         else:
#             print("No")
#     elif S[0] != S[2]:
#         if S.count(S[2]) == 2:
#             print("Yes")
#         else:
#             print("No")
# else:
#   print("No")

print(len(set(S)))