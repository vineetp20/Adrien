from imageai.Prediction.Custom import CustomImagePrediction
import os
import glob
ls=[]
img=[]
Coke=0
Pepsi=0
Sprite=0
Mirinda=0
execution_path = os.getcwd()

for i in os.listdir('Dataset/models/'):
    if i[:12] =='model_ex-100':
        a=i

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()

prediction.setModelPath(os.path.join(execution_path, 'Dataset/models/'+str(a)))       
prediction.setJsonPath(os.path.join(execution_path, "Dataset/json/model_class.json"))
prediction.loadModel(num_objects=4)
os.chdir(os.getcwd() + '/images')
exec_path=os.getcwd()

#exec_path = exec_path + '/images/'

for j in os.listdir('.'):
    
    if j.endswith('.jpg'):
            
        predictions, probabilities = prediction.predictImage(os.path.join(exec_path, j), result_count=1)
        img.append(predictions)
        if predictions==['Coke']:
            Coke=Coke+1
        if predictions==['Pepsi']:
            Pepsi=Pepsi+1
        if predictions==['Sprite']:
            Sprite=Sprite+1
        if predictions==['Mirinda']:
            Mirinda=Mirinda+1

print(img)
print("Count")
print("Pepsi: "+str(Pepsi))
print("Coke: "+str(Coke))
print("Mirinda: "+str(Mirinda))
print("Sprite: "+str(Sprite))
