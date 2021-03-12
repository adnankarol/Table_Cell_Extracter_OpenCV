from typing import List
import os, glob, cv2

class BoxAnnotation():
    
    def __init__(self,x: float, y:float, width: float, height: float, class_name: str):
        self.x = x
        self.y = y
        self.width = width # relative per img width
        self.height = height # relative per img height
        self.class_name = class_name
        
class TableAnalysis:

    config = {
        "parameter1": 42,
    }

    def process(self, filepath) -> List[BoxAnnotation]:
        
        box_annotations = []
        
        # TODO: Insert your code here, you can also write it in seperate files and call it from here
        
        # example which creates one cell that covers the whole image
        box_annotations.append(BoxAnnotation(x=0,y=0, width=1, height=1, class_name="cell-0-0"))
        
        return box_annotations

    
    def write_results(self,box_annotations: List[BoxAnnotation], filepath, outdir):
        
        image = cv2.imread(filepath, cv2.IMREAD_COLOR)
        image_height, image_width, num_channels = image.shape
        
        for annotation in box_annotations:
            
            x1 = max(0, int(annotation.x * image_width))
            y1 = max(0, int(annotation.y * image_height))
            x2 = min(image_width - 1, x1 + int(annotation.width * image_width))
            y2 = min(image_height - 1, y1 + int(annotation.height * image_height))

            cell = image[y1:y2, x1:x2, ...]
            os.makedirs(outdir, exist_ok=True)
            
            cv2.imwrite(os.path.join(outdir, annotation.class_name+".png"), cell)
              

    
    
if __name__ == "__main__":
    table_analysis = TableAnalysis()
    
    for filepath in glob.glob(os.path.join("tables/*.png")):
        box_annotations = table_analysis.process(filepath)
        outdir = os.path.join("results", os.path.basename(filepath).split(".")[0])
        table_analysis.write_results(box_annotations, filepath, outdir)
