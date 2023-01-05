const f = (s) => {
    const freq = {};
  
    for (const c of s) {
      const uppercaseC = c.toUpperCase();
      if (uppercaseC.match(/[A-Z]/)) {
        if (uppercaseC in freq) {
          freq[uppercaseC]++;
        } else {
          freq[uppercaseC] = 1;
        }
      }
    }
  
    const sortedFreq = Object.entries(freq).sort((a, b) => b[1] - a[1]);

    for (const [i, [c, f]] of sortedFreq.entries()) {
      if (i >= 5) {
        break;
      }
      const percentage = (f / s.replace(/[^A-Z]/ig, "").length) * 100;
      console.log(`${c}: ${percentage.toFixed(1)}%`);
    }
  }