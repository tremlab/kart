import React from 'react';

const KartItem = (props) => {
  const i = props.kartItem;
  const { item, quantity } = i;
  return (
    <div className="KartItem">
      <tr>
        <td>{ item }</td>
        <td>{ quantity }</td>
      </tr>
    </div>
  );
};

export default KartItem;
