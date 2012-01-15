import os
for root, dirs, files in os.walk('./'):
	for name in files:
		filename = os.path.join(root, name)
		print filename