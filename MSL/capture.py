import cv2
import os

LETTER = 'other'
save_dir = rf"D:\User\Documents\#UTM\SEMESTER 6\PSM1\InitialMSL\MSL\{LETTER}"
os.makedirs(save_dir, exist_ok=True)

print(f"Save directory: {save_dir}")
print(f"Existing images: {len(os.listdir(save_dir))}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open camera!")
else:
    print("Camera opened successfully!")
    print("Press SPACE to capture ONE image, Q to quit")

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read frame!")
        break

    cv2.imshow("Test Camera - Press SPACE to capture, Q to quit", frame)

    key = cv2.waitKey(1)
    if key == ord(' '):
        filename = os.path.join(save_dir, f"oher3_{count:04d}.jpg")
        cv2.imwrite(filename, frame)
        count += 1
        print(f"Saved: {filename}")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Done! Saved {count} images")