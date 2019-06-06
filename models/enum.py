from enum import Enum,unique

@unique
class BACKBONE(Enum):
    MOBILENET=0
    DARKNET53=1
    RESNET50=2