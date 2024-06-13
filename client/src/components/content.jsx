import flowers from '../assets/data/placeholderdata';
console.log(flowers)

export default function Content() {
    return (
        <div>
            {flowers && flowers.length 
            ? flowers.map(flower => 
                <div>

                    <p>{flower.name}</p>
                    <p>{flower.description}</p>
                    <p>{flower.price}</p>
                    <img src={flower.image_url} height={"300"} width={"300"}></img>
                </div>

        ) 
            : "Loading..."}
        </div>
    )
}