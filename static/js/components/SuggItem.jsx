import React from 'react';

const SuggItem = (props) => {
  const suggItem = props.suggItem;
  return (
    <option value={ suggItem }/>
  );
};

export default SuggItem;
