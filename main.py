import chromadb
import joblib
import pandas as pd


# client = chromadb.PersistentClient()

# collection = client.get_collection("applicants")

# scaler = joblib.load(r"C:\Users\andre\TyuiuDirectionsRecSys\notebooks\standard_scaler.joblib")

# df = pd.read_csv(r"C:\Users\andre\TyuiuDirectionsRecSys\notebooks\Applicant.csv")
# df.drop("Unnamed: 0", axis=1, inplace=True)

# applicants_df = df.drop("direction", axis=1)
# directions_df = df["direction"]

# directions = directions_df.to_numpy()

# scaled = scaler.transform(applicants_df)

# import uuid

# client = chromadb.PersistentClient(path=r"C:\Users\andre\TyuiuDirectionsRecSys\chroma")

# collection = client.get_collection("applicants")

# for vector, direction in zip(scaled, directions):
#     collection.add(
#         ids=[str(uuid.uuid4())],
#         embeddings=[vector.tolist()],
#         metadatas={"direction": direction},
#     )

scaler = joblib.load(r"C:\Users\andre\TyuiuDirectionsRecSys\notebooks\standard_scaler.joblib")
df = pd.read_csv(r"C:\Users\andre\TyuiuDirectionsRecSys\notebooks\Applicant.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
print(df.loc[0])
applicants_df = df.drop("direction", axis=1)
scaled_vector = scaler.transform(applicants_df)

client = chromadb.PersistentClient()
collection = client.get_collection("applicants")
results = collection.query(
    query_embeddings=scaled_vector[0]
)
print(results["metadatas"])