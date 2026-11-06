// Analytic bound powers only. No energies, training or theorem constants are computed.
function valid(x,name){if(!Number.isFinite(x)||x<0)throw new RangeError(name+' must be finite and nonnegative');}
export function sixthFreePowers(h,d=1){valid(h,'h');valid(d,'d');return[h,d,5*h/6+d/3,h/3+5*d/6];}
export function globalPhysicalState(theta){valid(theta,'theta');if(theta>1)throw new RangeError('theta must lie in [0,1]');
 const previousPowers=[theta,1+theta/6,2*(1+theta)/3],powers=[theta,1+theta/6,5*theta/6+1/3,theta/3+5/6];
 return{theta,powers,previousPowers,power:Math.max(...powers),previousPower:Math.max(...previousPowers),sixthFreePower:Math.max(...sixthFreePowers(theta)),targetGap:Math.max(...powers)-theta};
}
export function physicalBlockPowers(aj){if(!Array.isArray(aj)||aj.length!==6)throw new RangeError('Six factor exponents are required');for(const x of aj)valid(x,'factor exponent');
 const h=aj.slice(0,5).reduce((s,x,i)=>s+(i+1)*x,0),z=aj[5];return sixthFreePowers(h).map(x=>x+z);
}
