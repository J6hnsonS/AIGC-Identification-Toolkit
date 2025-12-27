from src.unified.watermark_tool import WatermarkTool

# 使用默认配置初始化
tool = WatermarkTool()

# 使用自定义配置初始化
tool = WatermarkTool(config_path="/inspire/ssd/project/short-term/250041219031/AIGC-Identification-Toolkit/src/video_watermark/videoseal/videoseal/cards/videoseal_1.0.yaml")

# 隐式水印（默认operation='watermark'）
marked_img = tool.embed("/inspire/ssd/project/short-term/250041219031/AIGC-Identification-Toolkit/training_dataset/images/1_127192.png", "abcdefg", 'image',
                       operation='visible_mark', position='bottom_right')

# 保存到文件
marked_img.save('marked_result2.jpg')  # 或 .png

img_wm = tool.embed(content="/inspire/ssd/project/short-term/250041219031/AIGC-Identification-Toolkit/training_dataset/images/1_127192.png", message="Img_01", modality='image')
img_wm.save('marked_result3.jpg')

