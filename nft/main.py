# from PIL import Image
# import os
#
# # img1 = Image.open("img1/2.png")
# images = ["img1", "img2", "img3", "img4"]
# all = []
# for image in images:
#     cur = []
#     for path in os.listdir(image):
#         full_path = os.path.join(image, path)
#         cur.append(Image.open(full_path))
#     all.append(cur)
# idx = 1
# for a in range():
#     for b in range(7):
#         for c in range(7):
#             for d in range(7):
#                 result = Image.alpha_composite(all[0][a], all[1][b])
#                 result = Image.alpha_composite(result, all[2][c])
#                 result = Image.alpha_composite(result, all[3][d])
#                 result.save(f'./result/image {idx}.png')
#                 idx += 1
# print("success")


# import random
# s = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
#
# x = s.split(' ')
# for _ in range(20):
#     random.shuffle(x)
#     print(''.join(x))
