console.log(`app.js가 연결되었습니다.`)

//데이터 받고 화면에 뿌리기
const data = {
    "id": 1,
    "productName": "버그를 Java라 버그잡는 개리씨 키링 개발자키링 금속키링",
    "price": 12500,
    "stockCount": 100,
    "thumbnailImg": "asset/img/1/thumbnailImg.jpg",
    "option": [],
    "discountRate": 0,
    "shippingFee": 1500,
    "detailInfoImage": [
    "asset/detail/2/detail1.png",
    "asset/detail/2/detail2.png"
    ],
    "viewCount": 0,
    "pubDate": "2022-02-28",
    "modDate": "2022-02-28"
}

const mainContainer = document.getElementById("main");
const BASE_URL = "http://test.api.weniv.co.kr/"


function createProductCard(imgUrl, price, productName, onClick) {

    //요소 만들기
    const $productCard = document.createElement("div");
    const $price = document.createElement("span")
    const $productName = document.createElement("strong");
    // const $image = document.createElement("img")
    
    //태그 내 글자 지정 받은 데이터의 특정부분으로
    $productName.innerText = productName;
    $price.innerText = price + `원`;
    // $image.src = imgUrl;
    // $productCard.append($image, $productName, $price);
    $productCard.append($productName, $price);
    $productCard.addEventListener("click", onClick);

    
    return $productCard

    // console.log(productName);
    // mainContainer.appendChild(image);
    // mainContainer.appendChild(price);
    // mainContainer.appendChild(productName);
    // mainContainer.appendChild(productCard);     일일히 다 띄우는 방법 귀찮음 >> 함수로 묶고 반복

}

function createProductDetail(imgUrl) {
    const $productDetail = document.createElement(`img`);  //이미지 태그 만들고 imgUrl 링크의 소스(이미지) 출력
    $productDetail.src = imgUrl;
    return $productDetail
}


async function main() {
    const productsContainer = document.createElement("div");
    productsContainer.id = "products";
    const detailContainer = document.createElement("div");
    detailContainer.id = "detail";
    mainContainer.appendChild(productsContainer)
    mainContainer.appendChild(detailContainer)

    const res = await fetch(BASE_URL+"mall");          //fetch값 res에 들어감. json
        const json = await res.json();
        console.log(json);
    
        
        // forEach 로 각 받아온 데이터의 배열안의 정보를 띄어준다.
        json.forEach(data => {
            const productId = data.id;
            const productimgUrl = BASE_URL + data.thumbnailImg;
            const productName = data.productName;
            const price = data.price;
            const onClick = async (e) => {  //event  async + await  >> promise로 return
                detailContainer.innerHTML = "" //클릭시 기존 detailcontainer안의 내용 초기화
                console.log(`${productId}번 상품이 클릭 되었습니다!`)
                const res = await fetch(BASE_URL + "mall/" + productId)
                const json = await res.json();
                json.detailInfoImage.forEach(imgUrl => {
                    const detailImgUrl = BASE_URL + imgUrl
                    const $productDetail = createProductDetail(detailImgUrl)
                    detailContainer.appendChild($productDetail)
                })
            }
            const $productCard = createProductCard(productimgUrl, price, productName, onClick)
            productsContainer.appendChild($productCard);
        })
    };
    


main();