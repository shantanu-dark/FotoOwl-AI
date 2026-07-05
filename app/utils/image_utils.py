import cv2
import os


def calculate_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()


def calculate_brightness(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv[:, :, 2].mean()


def image_score(path):

    image = cv2.imread(path)

    if image is None:
        return None

    h, w = image.shape[:2]

    resolution = h * w

    blur = calculate_blur(image)

    brightness = calculate_brightness(image)

    # Normalize resolution instead of letting it dominate
    resolution_score = min((resolution / 16000000) * 30, 30)

    blur_score = min(blur / 15, 35)

    brightness_score = (
        35
        - abs(brightness - 140) / 4
    )

    brightness_score = max(0, brightness_score)

    total = (
        resolution_score
        + blur_score
        + brightness_score
    )

    return {

        "image_name": os.path.basename(path),

        "path": path,

        "resolution": resolution,

        "quality_score": round(total, 2),

        "blur_score": round(blur, 2),

        "brightness": round(brightness, 2),

        "importance_score": round(total, 2)

    }