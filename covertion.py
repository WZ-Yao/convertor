def converting(feet,inches):
    meter=0
    meter=feet*0.3048+inches*0.0254
    return meter

if __name__=="__main__":
    total=converting(1,1)
    print(total)