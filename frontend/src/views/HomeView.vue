<template>
  <div class="section-hero">
    <v-container>
      <div class="justify-center align-center grid grid--2-cols">
        <div>
          <h1 class="title-hero">
            Make Your Life Easier, Faster, and More Efficient.
          </h1>
          <p class="mt-5 text-hero">
            You Cash Is An E-Wallet Provided By YouCash To Make Your Life,
            Financial Transactions & Errands Easier From Anywhere, Anytime With
            Just One Click!
          </p>
        </div>
        <div>
          <img src="@/assets/e-wallet-3.png" class="img-hero" />
        </div>
      </div>
    </v-container>
  </div>

  <div class="features-section mt-16">
    <div>
      <div class="grid-small grid--3-cols">
        <div class="card-feature">
          <img src="@/assets/fast-icon.png" class="icon-features" />
          <h3 class="title-card-features">Fast</h3>
          <p>
            Lorem ipsum dolor sit. Error, tempore impedit magni quibusdam veniam
            pariatur iste. Dolore ex illum ipsam tempore. Temporibus quidem
            vitae, non dicta tempora deleniti officiis sapiente.
          </p>
        </div>
        <div class="card-feature">
          <img src="@/assets/available.png" class="icon-features" />
          <h3 class="title-card-features">Available</h3>
          <p>
            Lorem ipsum dolor sit. Error, tempore impedit magni quibusdam veniam
            pariatur iste. Dolore ex illum ipsam tempore. Temporibus quidem
            vitae, non dicta tempora deleniti officiis sapiente.
          </p>
        </div>
        <div class="card-feature">
          <img src="@/assets/connection.png" class="icon-features" />
          <h3 class="title-card-features">Any Where</h3>
          <p>
            Lorem ipsum dolor sit. Error, tempore impedit magni quibusdam veniam
            pariatur iste. Dolore ex illum ipsam tempore. Temporibus quidem
            vitae, non dicta tempora deleniti officiis sapiente.
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div>
      <div class="wide-card align-center justify-center">
        <div>
          <img src="@/assets/e-wallet-1.jpg" class="img-features" />
        </div>
        <div>
          <h2 class="title-card-features">Easy Transactions</h2>
          <p>
            Lorem ipsum dolor sit. Error, tempore impedit magni quibusdam veniam
            pariatur iste. Dolore ex illum ipsam tempore. Temporibus quidem
            vitae, non dicta tempora deleniti officiis sapiente.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* General Styles */
.grid {
  display: grid;
  row-gap: 9.6rem;
  column-gap: 6.4rem;
}

.grid-small {
  display: grid;
  row-gap: 2rem;
  column-gap: 3rem;
}

.grid--2-cols {
  grid-template-columns: repeat(2, 1fr);
}

.grid--3-cols {
  grid-template-columns: repeat(3, 1fr);
}
/* ************************** */

.section-hero {
  background-color: #e9f4f0;
  padding: 2rem;
}

.title-hero {
  line-height: 1.05;
  font-size: 2.8rem;
}

.text-hero {
  color: #555;
  font-size: 1.2rem;
}

.img-hero {
  width: 100%;
}

.features-section {
  margin: 2rem 4rem;
}

.card-feature {
  padding: 0.5rem 2rem;
  text-align: center;
  border-radius: 5px;
  border: 1px solid #bcded3;
  box-shadow: 1px 5px 5px #bcded3a1;
  /* box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.05); */
}

.title-card-features {
  margin-top: 0.5rem;
  margin-bottom: 1rem;
}

.icon-features {
  box-sizing: border-box;
  padding: 0.5rem;
  width: 5rem;
  background-color: #bcded3;
  border-radius: 100%;
}

.container {
  margin: 6rem 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.wide-card {
  max-width: 60rem;
  padding: 1rem 2rem;
  border: 1px solid #eee;
  border-radius: 5px;
  box-shadow: 0.1rem 0.5rem 1rem #bcded3;

  display: grid;
  row-gap: 2rem;
  column-gap: 3rem;
  grid-template-columns: 1fr 2fr;
}

.img-features {
  width: 100%;
}

/*****************/
/* Media Queries */
/*****************/

/************************************/
/* BELOW 1024px (Landscape Tablets) */
/************************************/
@media (max-width: 64em) {
  .grid {
    column-gap: 4.8rem;
    row-gap: 6.4rem;
  }

  .features-section {
    margin: 1rem 2rem;
  }

  .wide-card {
    max-width: 50rem;
    column-gap: 2rem;
    grid-template-columns: 2fr 3fr;
  }
}

/***************/
/* BELOW 848px */
/***************/
@media (max-width: 53em) {
  .grid {
    row-gap: 2rem;
  }

  .grid--2-cols,
  .grid--3-cols {
    grid-template-columns: repeat(1, 1fr);
  }

  .section-hero {
    text-align: center;
  }

  .title-hero {
    font-size: 2.6rem;
  }

  .text-hero {
    font-size: 1.2rem;
  }

  .img-hero {
    width: 55%;
  }

  .card-feature {
    width: 70%;
    align-self: center;
    justify-self: center;
  }

  .wide-card {
    max-width: 35rem;
    padding: 1rem;

    row-gap: 2rem;
    column-gap: 2rem;
    grid-template-columns: 1fr 1fr;
  }
}

/***************/
/* BELOW 608px */
/***************/
@media (max-width: 38em) {
  .grid {
    row-gap: 1rem;
  }

  .title-hero {
    font-size: 1.8rem;
  }

  .text-hero {
    font-size: 1rem;
  }

  .img-hero {
    width: 75%;
  }

  .card-feature {
    width: 100%;
  }

  .wide-card {
    text-align: center;
    padding: 1rem;

    row-gap: 1rem;
    grid-template-columns: 1fr;
  }

  .img-features {
    width: 40%;
  }
}
</style>
