'use strict';
importScripts('../quantum-core.js','surface-core.js');
let prepared=null,modelKey=null;
self.onmessage=function(event){
 const {id,model,config}=event.data;
 try{
  const key=JSON.stringify(model);
  if(key!==modelKey){SurfaceCore.topology(model);prepared=new QuantumCore.StateVector(18).applyCircuit(model.prepare_circuit);modelKey=key;}
  const start=performance.now(),result=SurfaceCore.simulate(QuantumCore,model,config,prepared);
  result.wallMilliseconds=performance.now()-start;
  self.postMessage({id,result});
 }catch(error){self.postMessage({id,error:String(error.message||error)});}
};
